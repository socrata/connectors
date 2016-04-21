require 'colorize'
require 'httparty'
require 'json'

# Variables and setup
SHA = `git rev-parse --short HEAD`.strip
DATE = `git show --pretty="format:%at" HEAD | head -n 1`.strip
STAMP = <<-STAMP
define STAMP
{
  "sha" : "#{SHA}",
  "href" : "https://github.com/socrata/dev.socrata.com/commit/#{SHA}",
  "date" : #{DATE}
}
STAMP
URL = "https://dev-socrata-com-#{ENV['TRAVIS_BUILD_NUMBER'] || SHA}.surge.sh"

desc "clean up after ourselves"
task :clean do
  puts "Cleaning up after ourselves...".green
  sh "rm -rf public"
end


desc "perform a full jekyll site build"
task :jekyll do
  puts "Performing a full build...".green
  sh 'bundle exec jekyll build'
end

desc "perform an incremental jekyll build"
task :incremental do
  puts "Performing an incremental build...".green
  sh 'bundle exec jekyll build --incremental --safe'
end

desc "watch for changes and automatically rebuild (incrementally)"
task :watch do
  puts "Performing an incremental build...".green
  sh 'bundle exec jekyll build --incremental --safe --watch'
end

desc "automatically rebuild (incrementally), running a local server"
task :serve do
  puts "Performing an incremental build...".green
  sh 'bundle exec jekyll serve --incremental --safe --watch'
end

desc "create a build and version build.json file"
task :stamp do
  puts "Stamping build.json for #{SHA}...".green
  File.open("public/build.json", 'w') { |f| f.write(STAMP) }
end

desc "perform a quick build with a stamp"
task :quick => [:incremental, :stamp] do
end

desc "test links with htmlproof"
task :htmlproof => [:jekyll] do
  sh "bundle exec htmlproof ./public/ --only-4xx --check-html --href-ignore \"/#/,/\/foundry/,/\/register/,/APP_TOKEN/\""
end

desc "stage site to #{URL}"
task :stage => [:jekyll, :stamp, :rm_router] do
  puts "Staging content to #{URL}...".green
  sh "surge --project ./public --domain #{URL}"
end

desc "tear down site at #{URL}"
task :teardown do
  puts "Tearing down content at #{URL}...".green
  sh "surge --domain #{URL} teardown"
end

desc "allows you to clean up surge staged sites" 
task :surge_cleanup do
  sites = `surge list | grep dev-socrata-com`.lines.collect { |s| s.strip }

  puts "We will now " + "PERMANANTLY DELETE".on_red + " the following #{sites.count} sites:"
  sites.each { |s| puts " - #{s}" }

  print "Are you sure you want to do that? (y/N) ".green
  answer = STDIN.gets

  if answer.strip.downcase == "y"
    sites.each do |s|
      puts "Tearing down #{s}..."
      sh "surge --domain #{s} teardown"
    end
  else
    print "Aborted!".red
  end
end

desc "add a comment to a pull request with the staging URL, #{URL}"
task :tag_pull_request do
  response = HTTParty.post(
    "https://api.github.com/repos/#{ENV['TRAVIS_REPO_SLUG']}/issues/#{ENV['TRAVIS_PULL_REQUEST']}/comments",
    :body => {
      body: ":rocket: Site staged at #{URL}"
    }.to_json,
    :headers => {
      "Content-Type" => "application/json",
      "User-Agent" => "Travis Integration",
      "Authorization" => "token #{ENV['GITHUB_OAUTH_TOKEN']}"
    }
  )

  puts response.inspect
end

desc "run casperjs tests on #{URL}"
task :test do
  puts "Running casperjs tests on #{URL}...".green
  sh "BASE=#{URL} casperjs --ssl-protocol=any --ignore-ssl-errors=true --verbose --log-level=warning test _tests/test-*"
end

desc "clean up the ROUTER file, so we can push staging sites to Surge.sh"
task :rm_router do
  sh "rm public/ROUTER"
end

desc "perform a full test cycle to #{URL}"
task :staging_test => [:clean, :jekyll, :htmlproof, :stamp, :rm_router, :stage, :test] do
  puts "Done!!!".on_green
end
